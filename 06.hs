-- ghc --make -O2 06

checkForHappiness' list1 = checkForHappiness list1 []

checkForHappiness :: [Int] -> [Int] -> Int
checkForHappiness list1 list2
    | list1 == [] = 0
    | sum list1 == sum list2 = 1
    | otherwise = checkForHappiness (tail list1) (head list1:list2)

result = sum (map (checkForHappiness') [[a1,a2,a3,a4,a5,a6,a7, a8] | 
                        a1 <- [0..4], 
                        a2 <- [0..4], 
                        a3 <- [0..4], 
                        a4 <- [0..4], 
                        a5 <- [0..4], 
                        a6 <- [0..4], 
                        a7 <- [0..4], 
                        a8 <- [0..4]
                        ])

main = print result
