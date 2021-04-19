from Aula06.Pessoas.model.Pessoa import Pessoa
from Aula06.Pessoas.model.Juridica import Juridica
from Aula06.Pessoas.model.Fisica import Fisica

print("\n -------------- Pessoa Normal -----------------")
Pnormal1 = Pessoa(1, 'Fabio', 'Rua Peru', 99023912)
Pnormal1.imprime_nome()
print(Pnormal1.verTelefone)

print("\n -------------- Pessoa Juridica -----------------")
Pjuridica1 = Juridica(1, 'Jaime', 'Rua Peru', 99023912,'03930192' ,'0090',20)
Pjuridica1.imprime_nome()
Pjuridica1.imprime_CNPJ()


print("\n ---------------- Pessoa Fisica -------------------")
Pfisica1 = Fisica(1, 'Jairo', 'Rua Peru', 99023912, '03777721', 23, 80.0, 1.60)
Pfisica1.imprime_nome()
Pfisica1.imprime_CPF()

