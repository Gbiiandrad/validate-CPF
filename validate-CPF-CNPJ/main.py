from Cpf_Cnpj import CpfCnpj
# from validate_docbr import CNPJ

# verificar se o CPF tem 11 digitos
# cpf_um = Cpf("15316264754")
# print(cpf_um)

# CNPJ
exemplo_cnpj = "35379838000112"
exemplo_cpf = "32007832062"
# cnpj = CNPJ()
# print(cnpj.validate(exemplo_cnpj))
documento = CpfCnpj(exemplo_cpf, 'cpf')
print(documento)
