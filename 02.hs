import System.IO  
import Data.Char
import Data.List.Split

letters = ' ':['a'..'z']

prepareData :: String -> [[String]]
prepareData d =  endBy ["Nice"] $ filter (`elem` ["Yo","Nice"]) $ words $ filter (`elem` ' ':['a'..'z']++['A'..'Z']) d

decode :: [[String]] -> [Char]
decode [] = ""
decode (x:xs) = [letters !! length x] ++ decode xs

main = do
    handle <- openFile "data/02.data" ReadMode  
    contents <- hGetContents handle    
    putStr $ decode $ prepareData contents
    hClose handle    