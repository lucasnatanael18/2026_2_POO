import java.util.*;

class Viagem { 
    double distancia;
    int horas;
    int minutos;

    double calcVM() { 
        double tempoHoras = horas + (minutos / 60.0);
        return distancia / tempoHoras;
    }
}

public class Main {
    public static void main(String[] args) { 
        Scanner entrada = new Scanner(System.in);
        Viagem viagem = new Viagem();

        System.out.println("Digite a distancia em KM: ");
        viagem.distancia = entrada.nextDouble();

        System.out.println("Digite as horas: ");
        viagem.horas = entrada.nextInt();

        System.out.println("Digite os minutos: ");
        viagem.minutos = entrada.nextInt();

        double velocidade = viagem.calcVM(); 
      
        System.out.println("Velocidade média: " + velocidade + " KM/H"); 
        
        entrada.close();
    }
}
