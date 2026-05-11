package sem_template_method;

public class Main {

    public static void main(String[] args) {
        System.out.println("========================================");
        System.out.println("          SEM TEMPLATE METHOD           ");
        System.out.println("========================================\n");

        // Sem abstração: dependemos diretamente das classes concretas
        RelatorioPDF pdf = new RelatorioPDF();
        System.out.println("-> Gerando: RelatorioPDF");
        pdf.gerarRelatorio();
        System.out.println();

        RelatorioExcel excel = new RelatorioExcel();
        System.out.println("-> Gerando: RelatorioExcel");
        excel.gerarRelatorio();
        System.out.println();

        System.out.println("Problemas:");
        System.out.println("  x Manutenção difícil (mudança na ordem = alterar N classes)");
        System.out.println("  x Alto risco de inconsistência (buscarDados duplicado)");
        System.out.println("  x Baixa extensibilidade (novo formato copia tudo)");
        System.out.println("  x Maior complexidade acidental");
    }
}
