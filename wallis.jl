function wallis(n) 
    pi_ = 2.0
    tmp_ = 0.0
    for i = 1:n
       tmp_ = 4.0*i^2.0
       pi_ *= tmp_/(tmp_-1); 
    end
    return pi_
end

function main()
    n = 1000000
    res = wallis(n)
    println("$n = $res")
end

main()
