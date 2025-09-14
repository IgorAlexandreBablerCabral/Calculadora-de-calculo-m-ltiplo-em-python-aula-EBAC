# calculadora Py 2 numeros 
import unicodedata
import tkinter as tk
from tkinter import messagebox

#criar janela
janela = tk.Tk()
janela.title("Janela Calculadora")
janela.geometry("800x900")

#Label texto explicativo para o usuario
texto = "Nessa experiencia matematica você irá realizar os calculos de:\n - adição\n - subtração\n - multiplicação\n - divisão com a exibição do resto e quociente.\n Essa calculadora, além de exibir quais dos dois números calculados é o maior,\n também exibe um aviso caso seu resultado for maior que 999"
label = tk.Label(janela, text=texto, wraplength=780, justify="left")
label.pack(pady=20)

#Label texto explicativo para o usuario inserção do primeiro número
label_num1 = tk.Label(janela, text="Digite aqui o primeiro valor a ser calculado: ")
label_num1.pack(pady=5)

#Input no Front para receber o valor
entry_num1 = tk.Entry(janela)
entry_num1.pack(pady=5)

#Label texto inserção do segundo número
label_num2 = tk.Label(janela, text="Digite aqui o segundo valor a ser calculado: ")
label_num2.pack(pady=5)
entry_num2 = tk.Entry(janela)
entry_num2.pack(pady=5)

def verificar_valor_e_calcular():
    try:
        num_1 = float(entry_num1.get()) #convertendo para float para não existir nenhum caso de erro
    except ValueError: #caso não seja um núemro apontar esse erro
        messagebox.showerror("Erro", f"O valor inidicado na primeira inserção '{entry_num1.get()}' não é um número")
        return
    try:
        num_2 =float(entry_num2.get())
    except ValueError: #caso não seja um número apontar esse erro
        messagebox.showerror("Erro", f"O valor indicado na segunda inserção '{entry_num2.get()}' não é um número")
        return

    
    if num_2 >999:
            messagebox.showwarning("Aviso", "o valor da segunda inserção digitada é maior que 999!")
    if num_1 > 999:
            messagebox.showwarning("Aviso","o valor da primeira inserção digitada é maior que 999!")

    # Calculando resultados
    soma = num_1 + num_2
    sub = num_1 - num_2
    mult = num_1 * num_2
    div = num_1 / num_2 if num_2 != 0 else "Indefinido"
    resto = num_1 % num_2 if num_2 != 0 else "Indefinido"
    quociente = num_1 // num_2 if num_2 != 0 else "Indefinido"
    maior =max(num_1, num_2)
    
    #Aviso Resultado maior que 999
    aviso_resultado_maior_que_999 = ""
    if any(isinstance(x, (int, float)) and x > 999 for x in [soma, sub, mult, div if isinstance(div, (int,float)) else 0]):
        aviso_resultado_maior_que_999 = " Algum dos resultados é maior que 999!!"
    
    #Resultados
    resultados = ( 
         f"Soma: {soma}\n"
         f"Subtração: {sub}\n"
         f"Multiplicação: {mult}\n"
         f"Divisão: {div}\n"
         f"Resto da Divisão: {resto}\n"
         f"Quociente: {quociente}\n"
         f"Maior número digitado {maior}"
         + aviso_resultado_maior_que_999
    )
    messagebox.showinfo("Resultado", resultados)

# Botão para a realização dos calculos
botao = tk.Button(janela, text ="Calcular", command=verificar_valor_e_calcular)
botao.pack(pady=20)

#Label de aviso para os professores que vão corrigir minha tarefa <3
texto = "Olá professores da EBAC lindos do meu coração, como foi minha primeira exp com Tkinter (essa interface de front simplificada de Python), dentro desse projeto ocorreram alguns bugs satânicos e eu precisei da ajuda do chatGpt para a correção deles, não me matem <3 amo vcs"
label = tk.Label(janela, text=texto, wraplength=800, justify="center")
label.pack(pady=20)

# Cria a mensagem de resultado
janela.mainloop()