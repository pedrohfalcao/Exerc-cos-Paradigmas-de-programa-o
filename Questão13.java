class Matematica {
    public static int fatorial(int n) {
        if (n == 0) {
            return 1;
        }
        int resultado = 1;
        for (int i = 1; i <= n; i++) {
            resultado *= i;
        }
        return resultado;
    }
}

public class Main {
    public static void main(String[] args) {
        int numero = 5;
        System.out.printf("O fatorial de %d é %d%n", numero, Matematica.fatorial(numero));
    }
}
