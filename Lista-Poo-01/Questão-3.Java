import java.util.Scanner;

class ContaBancaria {
    String titular;
    int nConta;
    double saldo;

    void depositar(double valor) {
        saldo = saldo + valor;
    }

    void sacar(double valor) {
        if (valor <= saldo) {
            saldo = saldo - valor;
        } else {
            System.out.println("Saldo Insuficiente");
        }
    }

    void verificarSaldo() {
        System.out.println("Saldo atual: R$ " + saldo);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        while (true) {
            System.out.println("SISTEMA BANCÁRIO - NOVA SESSÃO");
            
            ContaBancaria conta = new ContaBancaria();

            System.out.println("Digite o nome do titular: ");
            conta.titular = entrada.nextLine();

            System.out.println("Digite o número da conta:");
            conta.nConta = entrada.nextInt();

            System.out.println("Digite o saldo inicial: ");
            conta.saldo = entrada.nextDouble();
            entrada.nextLine();

            while (true) {
                System.out.println("\nEscolha a operação que deseja:");
                System.out.println("1 - Depositar");
                System.out.println("2 - Sacar");
                System.out.println("3 - Verificar Saldo");
                System.out.println("4 - Finaliar operação");
                System.out.print("Opção: ");
                
                int opcao = entrada.nextInt();
                entrada.nextLine();

                if (opcao == 1) {
                    System.out.println("Digite o valor que deseja depositar: ");
                    double valor = entrada.nextDouble();
                    entrada.nextLine(); 
                    conta.depositar(valor);
                    System.out.println("Depósito realizado com sucesso!");
                    conta.verificarSaldo();

                } else if (opcao == 2) {
                    System.out.println("Digite o valor que deseja sacar: ");
                    double valor = entrada.nextDouble();
                    entrada.nextLine(); 
                    conta.sacar(valor);
                    conta.verificarSaldo();

                } else if (opcao == 3) {
                    conta.verificarSaldo();

                } else if (opcao == 4) {
                    System.out.println("\nSessão de " + conta.titular + " finalizada.");
                    System.out.println("Redirecionando para a criação de uma nova conta...");
                    break;
                } else {
                    System.out.println("Opção inválida!");
                }
            }
        }
    }
}
