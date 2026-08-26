import java.util.*;

class Circulo {
    double raio;

    double calcularArea() {
        return Math.PI * raio * raio;
    }

    double calcularCircuferencia() {
        return 2 * Math.PI * raio;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Circulo circulo = new Circulo();

        System.out.print("Digite o raio: ");
        circulo.raio = scanner.nextDouble();

        System.out.println("Area: " + circulo.calcularArea());
        System.out.println("Circunferencia: " + circulo.calcularCircuferencia());

        scanner.close();
    }
}