int main() {
    int a = 0;
    int b = 200;
    int soma = a + b;
    int vet[] = {1, 2, 3, 4, 5};

    while(soma != 1) {
        soma = soma / 100;
    }
    
    if (soma > 100) {
        return soma;
    } else {
        return soma - 100;
    }
}