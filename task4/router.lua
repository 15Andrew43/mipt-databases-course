local vshard = require('vshard')
function put(id, balance, price, status)
    local bucket_id = vshard.router.bucket_id_mpcrc32({ id })
    vshard.router.callrw(bucket_id, 'insert_user', { id, bucket_id, balance, price, status })
end

function get(id)
    local bucket_id = vshard.router.bucket_id_mpcrc32({ id })
    return vshard.router.callro(bucket_id, 'get_user', { id })
end

function insert_data()
    put(1, 100, 1, false)
    put(2, 100, 1, false)
    put(3, 10, 0.5, false)
end

function add_balance(id, money)
    local bucket_id = vshard.router.bucket_id_mpcrc32({ id })
    return vshard.router.callrw(bucket_id, 'add_user_balance', { id, money })
end

function set_price(id, new_price)
    local bucket_id = vshard.router.bucket_id_mpcrc32({ id })
    return vshard.router.callrw(bucket_id, 'set_user_price', { id, new_price })
end