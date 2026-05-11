package sem_template_method;

public class RelatorioPDF {

    public void gerarRelatorio() {
        buscarDados();      
        processarDados();
        gerarSaida();
    }

    private void buscarDados() {
        System.out.println("  [PDF] Buscando dados do banco de dados...");
    }

    private void processarDados() {
        System.out.println("  [PDF] Formatando dados em estrutura de páginas...");
    }

    private void gerarSaida() {
        System.out.println("  [PDF] Exportando arquivo relatorio.pdf");
    }
}
