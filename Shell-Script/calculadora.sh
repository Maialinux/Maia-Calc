#!/bin/bash

read -p "Digite um número: " n1

echo "Escolha o número do seu operador:"

read -p "1-somar | 2-subtrair | 3-multiplicar | 4-dividir: " operador

read -p "Digite o segundo número: " n2

if [ $operador -eq 1 ]
then
  resultado=`echo "scale=2; $n1 + $n2" | bc`
  echo "O resultado de $n1 + $n2 é = $resultado" 

elif [ $operador -eq 2 ]
then
  resultado=`echo "scale=2; $n1 - $n2" | bc`
  echo "O resultado de $n1 - $n2 é = $resultado" 

elif [ $operador -eq 3 ]
then
  resultado=`echo "scale=2; $n1 * $n2" | bc`
  echo "O resultado de $n1 * $n2 é = $resultado" 

elif [ $operador -eq 4 ]
then
  resultado=`echo "scale=2; $n1 / $n2" | bc`
  echo "O resultado de $n1 / $n2 é = $resultado" 

else
  echo "Nenhuma operação válida foi encontrada."

fi
