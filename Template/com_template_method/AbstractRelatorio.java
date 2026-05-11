package com_template_method;

public abstract class AbstractRelatorio {

    public final void gerarRelatorio() {
        buscarDados();
        processarDados();
        gerarSaida();
    }

    protected void buscarDados() {
        System.out.println("  [Base] Buscando dados do banco de dados...");
    }

    protected abstract void processarDados();
    protected abstract void gerarSaida();
}
