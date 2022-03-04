import utilidadesCeV.moeda as moeda
import utilidadesCeV.dados as dados

p = dados.leiadinheiro('digite o preço: R$')

moeda.resumo(p, 10, 5)