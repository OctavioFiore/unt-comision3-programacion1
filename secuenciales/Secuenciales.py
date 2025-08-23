#✓ Pedir al usuario el monto total de la cuenta. 
#✓ Calcular la propina sugerida al 10%. 
#✓ Calcular la propina sugerida al 15%. 
#✓ Calcular el total a pagar en ambos casos (cuenta + propina). 
#✓ Mostrar todos los resultados en pantalla
monto_total=float(input("Ingrese el monto de la cuenta: "))


descuento_diez=monto_total*0.10

propina_del_diez=monto_total-descuento_diez
print(f'Proprina sugerida(10%):{propina_del_diez}')

descuento_quince=monto_total*0.15

propina_del_quince=monto_total-descuento_quince
print(f'Proprina sugerida(15%):{propina_del_quince}')















