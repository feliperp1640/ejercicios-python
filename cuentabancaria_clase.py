class CuentaBancaria:
    def __init__(self,saldo):
        self.saldo = saldo

    def depositar(self,monto):
        self.saldo=self.saldo + monto
    
    def mostrar_saldo(self):
        print(f"El saldo actual es {self.saldo} pesos") 

saldo1 = CuentaBancaria(25000)
saldo1.mostrar_saldo()      # antes de depositar
saldo1.depositar(5000)
saldo1.mostrar_saldo()      # después — debe ser 30000

saldo2 = CuentaBancaria(45000)
saldo2.mostrar_saldo()