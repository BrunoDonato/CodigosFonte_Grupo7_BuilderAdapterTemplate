package sem_template_method;

public class RelatorioExcel {

    public void gerarRelatorio() {
        buscarDados();       
        processarDados();
        gerarSaida();
    }

    private void buscarDados() {
        System.out.println("  [Excel] Buscando dados do banco de dados...");
    }

    private void processarDados() {
        System.out.println("  [Excel] Organizando dados em linhas e colunas...");
    }

    private void gerarSaida() {
        System.out.println("  [Excel] Exportando arquivo relatorio.xlsx");
    }
}
