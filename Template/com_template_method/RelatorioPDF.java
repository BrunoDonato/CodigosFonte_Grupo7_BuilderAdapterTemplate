package com_template_method;

public class RelatorioPDF extends AbstractRelatorio {

    @Override
    protected void processarDados() {
        System.out.println("  [PDF] Formatando dados em estrutura de páginas...");
    }

    @Override
    protected void gerarSaida() {
        System.out.println("  [PDF] Exportando arquivo relatorio.pdf");
    }
}
