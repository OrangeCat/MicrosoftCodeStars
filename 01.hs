factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n - 1)

result = factorial 104 * 10 `div` 60 `div` 60

main :: IO ()
main = print result
