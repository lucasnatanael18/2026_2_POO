import java.util.*;

class ContaBancaria {
    String titular;
    int nConta;
    double saldo;
    double saque;

    void depositar(double valor) {
        saldo = saldo + valor;
    
    }
    void sacar(double valor) {
        if (valor <= saldo) {
            saque = saldo - valor;
        } else {
            System.out.println("Saldo Insuficiente");
        }

    }

    void verificarSaldo() {
    System.out.println("Saldo atual: R$ " + saldo);
    }
}

public class Main {
  public static void main(String [] args) {
    Scanner entrada = new entrada (System.in);
      ContaBancaria conta = new ContaBancaria();

      System.out.println("Digite o nome do titular: ");
      conta.titular = entrada nextLine();

      System.out.println("Digite o numero da conta:");
      conta.numero = entrada nextInt();

      System.out.println("Digite o saldo inicial: ");
      conta.saldo = entrada nextDouble();

      System.out.println("Escolha a operação que deseja");
      System.out.println("1 - Depositar");
      System.out.println("2 - Sacar");
      System.out.println("3 - Verificar Saldo");
      System.out.println("Opção: ");

      int Opção = entrada nextInt();

      if (Opção == 1) {
        System.out.println("Digite o valor que deseja depositar: ");
        double valor = nextDouble();
        conta.depositar (valor);
      }
    
      if (Opção == 2) {
        System.out.println("Digite o valor que deseja sacar: ");
        double valor = nextDouble();
        conta.sacar (valor;)
      }
      
      if (Opção == 3) {
        System.out.println(saldo);
      }

  }
}