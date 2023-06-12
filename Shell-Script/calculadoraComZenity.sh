#!/bin/bash

n1=`zenity --entry --title="Insira um número" --text="Insira um número" --width=300 --height=175`

zenity --info --title="Escolha uma operação" --text="Escolha o número do seu operador:" --width=300 --height=175

operador=`zenity --entry --title="Operadores" --text="1-somar | 2-subtrair | 3-multiplicar | 4-dividir:" --width=300 --height=175`

n2=`zenity --entry --title="Insira segundo número" --text="Insira segundo número" --width=300 --height=175`


if [ $operador -eq 1 ]
then
  resultado=`echo "scale=2; $n1 + $n2" | bc`
  zenity --info --title="Resultado Final" --text="O resultado de $n1 + $n2 é = $resultado" --width=300 --height=175 

elif [ $operador -eq 2 ]
then
  resultado=`echo "scale=2; $n1 - $n2" | bc`
  zenity --info --title="Resultado Final" --text="O resultado de $n1 - $n2 é = $resultado" --width=300 --height=175

elif [ $operador -eq 3 ]
then
  resultado=`echo "scale=2; $n1 * $n2" | bc`
  zenity --info --title="Resultado Final" --text="O resultado de $n1 * $n2 é = $resultado" --width=300 --height=175

elif [ $operador -eq 4 ]
then
  resultado=`echo "scale=2; $n1 / $n2" | bc`
  zenity --info --title="Resultado Final" --text="O resultado de $n1 / $n2 é = $resultado" --width=300 --height=175

else
  zenity --warning --title="Operação inválida" --text="Nenhuma operação válida foi encontrada." --width=300 --height=175

fi
