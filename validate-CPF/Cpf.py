from validate_docbr import CPF

#formatação e validação de cpf
class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_Valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF invalido")
        

    def cpf_Valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de digitos invalida!")
        
    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    
    def __str__(self):
        return self.format_cpf()