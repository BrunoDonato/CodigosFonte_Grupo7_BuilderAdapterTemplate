package com_template_method;

public class RelatorioExcel extends AbstractRelatorio {

    @Override
    protected void processarDados() {
        System.out.println("  [Excel] Organizando dados em linhas e colunas...");
    }

    @Override
    protected void gerarSaida() {
        System.out.println("  [Excel] Exportando arquivo relatorio.xlsx");
    }
}
