expirationd = require('expirationd')
fiber = require('fiber')
log = require('log')

box.schema.create_space('users', {
    format = {
        { name = 'id',               type = 'unsigned' },
        { name = 'bucket_id',        type = 'unsigned' },
        { name = 'balance',          type = 'double' },
        { name = 'price',      type = 'double' },
        { name = 'status',       type = 'boolean' },
        { name = 'last_update_time', type = 'double' },
    },
    if_not_exists = true
})

box.space.users:create_index('id', { parts = { 'id' }, if_not_exists = true })
box.space.users:create_index('bucket_id', { parts = { 'bucket_id' }, unique = false, if_not_exists = true })

function insert_user(id, bucket_id, balance, price, status)
    box.space.users:insert({ id, bucket_id, balance, price, status, fiber.time() })
end

function get_user(id)
    local tuple = box.space.users:get(id)
    if tuple == nil then
        return nil
    end
    return { tuple.id, tuple.balance, tuple.price, tuple.status, tuple.last_update_time }
end

function get_money_spend(price, last_update_time)
    local money_spend = price * (fiber.time() - last_update_time)
    return money_spend
end

function set_user_last_update_time(id, time)
    box.space.users:update(id, { { '=', 6, time } })
    return true
end

function set_user_price(id, new_price)
    box.space.users:update(id, { { '=', 4, new_price } })
    set_user_last_update_time(id, fiber.time())
    return true
end

function set_user_balance(id, new_balance)
    box.space.users:update(id, { { '=', 3, new_balance } })
    set_user_last_update_time(id, fiber.time())
    return true
end

function add_user_balance(id, money)
    box.space.users:update(id, { { '+', 3, money } })
    set_user_last_update_time(id, fiber.time())
    return true
end

function change_user_status(id, status)
    box.space.users:update(id, { { '=', 5, status } })
    set_user_last_update_time(id, fiber.time())
    return true
end

function add_user_balance(id, money)
    local user = get_user(id)
    local new_balance = user[2] + money
    set_user_balance(id, new_balance)
    change_user_status(id, true)
    return true
end

function is_expired(args, tuple)
    if tuple.status == false then
        return false
    end
    local money_spend = get_money_spend(tuple.price, tuple.last_update_time)
    if money_spend > tuple.balance then
        set_user_balance(tuple.id, 0.0)
        change_user_status(tuple.id, false)
        return true
    else
        set_user_balance(tuple.id, tuple.balance - money_spend)
        return false
    end
end

function delete_tuple(space, args, tuple)
    local user = tuple[2]
    set_user_price(user.id, 0)
    set_user_balance(user.id, 0)
    local http_client = require('http.client').new()
    http_client.request('GET', 'https://example.com' .. tostring(user.id))
end

expirationd.start("clean_tuples", box.space.users.id, is_expired, {
    process_expired_tuple = delete_tuple,
    args = nil,
    tuples_per_iteration = 50,
    full_scan_time = 3600
})