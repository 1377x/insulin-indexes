import math

glucosa_mg = input("Valor de glucosa (mg/dL): ")
insulina_ayunas = input("Valor de insulina (µIU/mL): ")
glucosa_mol = input("Valor de glucosa (mmol/L): ")
glucosa= float(glucosa_mg)
glucosam = float(glucosa_mol)
insulina= float(insulina_ayunas)


#Homa normal
if glucosa > 0:
    def Homa_ir_mg(glu, ins):
        resultado = (glu*ins)/405
        return resultado
    print("HOMA-IR: ", round(Homa_ir_mg(glucosa, insulina), 2))
else:
    def Homa_ir_mol(glu, ins):
        resultado = (glu*ins)/22.5
        return resultado
    print("HOMA-IR: ", round(Homa_ir_mol(glucosam, insulina), 2))


#Homa beta
if glucosa > 0: 
    def Homa_b_mg(glu, ins):
        resultado = (360*ins)/(glu-63)
        return resultado
    print("HOMA-B: ", round(Homa_b_mg(glucosa, insulina), 2))
else:
    def Homa_b_mol(glu, ins):
        resultado = (20*ins)/(glu-3.5)
        return resultado
    print("HOMA-B: ", round(Homa_b_mol(glucosam, insulina), 2))


if glucosa == 0:
    glucosa = glucosam * 18.016

def Quicki(glu, ins):
    resultado = 1/(math.log10(ins)+math.log10(glu))
    return resultado

def Spina_gr(glu, ins):
    g1 = 154.93
    dr = 1.6
    ge = 50.0
    p8 = 150.0
    a = g1*(p8*(dr+ins))
    b = ge*ins*glu
    c = dr/(ge*ins)
    d = 1/ge
    resultado = (a/b)-c-d
    return resultado

def Spina_gbeta(glu, ins):
    db = 7
    g3 = 58.8
    resultado = (ins*(db+glu))/(g3*glu)
    return resultado


print("QUICKI: ", round(Quicki(glucosa, insulina), 2))
print("SPINA-GR: ", round(Spina_gr(glucosa, insulina), 2))
print("SPINA-GB: ", round(Spina_gbeta(glucosa, insulina), 2))



