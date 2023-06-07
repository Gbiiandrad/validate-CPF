from validate_docbr import CPF, CNPJ

# formatação e validação de cpf


class CpfCnpj:
    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento)

        if self.tipo_documento == "cpf":
            if self.cpf_Valido(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF invalido")

        # para CNPJ
        elif self.tipo_documento == "cnpj":
            if self.cnpj_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ invalido")

        else:
            raise ValueError("Documento invalido!")

    def cpf_Valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de digitos invalida!")

    # Cnpj

    def cnpj_valido(self, cnpj):
        if len(cnpj) == 14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)
        else:
            raise ValueError("Quantidade de digitos invalida!")

    # mascara para CPF e CNPJ
    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def __str__(self):
        if self.tipo_documento == "cpf":
            return self.format_cpf()

        elif self.tipo_documento == "cnpj":
            return self.format_cnpj()
