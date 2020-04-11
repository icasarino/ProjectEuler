import Data.List
import Data.Maybe

suma1 = (+) 1
mult3 = (*) 3


calc n |odd n = (suma1.mult3) n
       |otherwise = div n 2

crtList 2 xs = xs ++ [1]
crtList n xs = crtList (calc n) (xs ++ [(calc n)])

getList = map (length.(flip crtList []))

algoritmo xs = 1 + (fromJust (elemIndex (maximum (getList xs)) (getList xs)))

main = print algoritmo [1..999999]