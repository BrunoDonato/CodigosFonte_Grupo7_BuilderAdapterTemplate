package com_template_method;

public class Main {

    public static void main(String[] args) {
        System.out.println("========================================");
        System.out.println("       COM TEMPLATE METHOD + SOLID      ");
        System.out.println("========================================\n");

        AbstractRelatorio[] relatorios = {
            new RelatorioPDF(),
            new RelatorioExcel()
        };

        for (AbstractRelatorio relatorio : relatorios) {
            System.out.println("-> Gerando: " + relatorio.getClass().getSimpleName());
            relatorio.gerarRelatorio();
            System.out.println();
        }

        System.out.println("Vantagens:");
        System.out.println("  + Reuso de código (buscarDados definido uma vez)");
        System.out.println("  + Padronização do processo (ordem garantida pelo template)");
        System.out.println("  + Baixa duplicação");
        System.out.println("  + Manutenção simples");
        System.out.println("  + Extensível: novo formato = nova subclasse, sem tocar no resto");
    }
}
