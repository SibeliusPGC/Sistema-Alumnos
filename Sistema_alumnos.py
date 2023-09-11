import tkinter as tk

lista_alumnos={}
turnos=["Mañana","Tarde","Noche","noche","mañana","tarde"]

def consulta_lista()://Funcion para el boton de consulta de alumnos por lista
    if lista_alumnos:
            print("----- Inicio de Listado -----\n")
            for nombre_alumno in lista_alumnos:
                print("Nombre: "+nombre_alumno+" - "
                +str(lista_alumnos[nombre_alumno][0])+" cursos. "
                +"Turno: "+lista_alumnos[nombre_alumno][1])
            print("\n----- Fin de Listado -----\n")
    else:
        ventana_error1=tk.Toplevel(ventana)
        ventana_error1.title(" *** Error! *** ")
        ventana_error1.config(width=250, height=100)
        et_con_datos=tk.Label(ventana_error1,text=" -- No hay alumnos ingresados -- ")
        et_con_datos.place(x=25, y=35)
            
def agregar()://Funcion para el alta de un alumno nuevo
        nombre_alumno=caja_nombre.get()
        cant_cursos=caja_cursos.get() 
        turno_alumno=caja_turno.get()

        if nombre_alumno.isalpha()==False:
            ventana_error2=tk.Toplevel(ventana)
            ventana_error2.title(" *** Error! *** ")
            ventana_error2.config(width=350, height=100)

            et_error2=tk.Label(ventana_error2,text=" X   * ERROR DEBE INGRESAR UN NOMBRE VALIDO *   X ")
            et_error2.place(x=25, y=40)
                       
        elif turno_alumno not in(turnos):
            ventana_error3=tk.Toplevel(ventana)
            ventana_error3.title(" *** Error! *** ")
            ventana_error3.config(width=350, height=100)

            et_error3=tk.Label(ventana_error3,text=" X   * ERROR Los turnos son: Mañana, Tarde o Noche *   X ")
            et_error3.place(x=20, y=35)
                         
        elif cant_cursos.isdigit() ==False:
            ventana_error4=tk.Toplevel(ventana)
            ventana_error4.title(" *** Error! *** ")
            ventana_error4.config(width=400, height=100)

            et_error4=tk.Label(ventana_error4,text=" X   * ERROR El alumno debe ser inscripto en algun curso *   X ")
            et_error4.place(x=25, y=35)
            
        elif int(cant_cursos)>4:
            ventana_error5=tk.Toplevel(ventana)
            ventana_error5.title(" *** Error! *** ")
            ventana_error5.config(width=430, height=100)

            et_error5=tk.Label(ventana_error5,text=" X   * ERROR El alumno no puede ser inscripto en mas de 4 cursos *   X ")
            et_error5.place(x=25, y=35)
            
                              
        else:
            lista_alumnos[nombre_alumno]=[cant_cursos,turno_alumno]
            print("\nNombre ingresado correctamente!\n")

def consulta_cursos()://Funcion para el boton de consulta de cursos
    alumno_consulta=caja_ver_gral.get()
    if alumno_consulta.isalpha()==False:
        ventana_error6=tk.Toplevel(ventana)
        ventana_error6.title(" *** Error! *** ")
        ventana_error6.config(width=350, height=100)

        et_error6=tk.Label(ventana_error6,text=" X   * ERROR DEBE INGRESAR UN NOMBRE VALIDO *   X ")
        et_error6.place(x=25, y=35) 

    else:
        print("Nombre: "+ alumno_consulta + " -- "+ "Cantidad de Cursos: "+ str(lista_alumnos[alumno_consulta][0]))            
            
def consulta_turnos()://Funcion para el boton de consulta turnos
    alumno_consulta=caja_ver_gral.get()
    if alumno_consulta.isalpha()==False:
        ventana_error7=tk.Toplevel(ventana)
        ventana_error7.title(" *** Error! *** ")
        ventana_error7.config(width=350, height=100)

        et_error7=tk.Label(ventana_error7,text=" X   * ERROR DEBE INGRESAR UN NOMBRE VALIDO *   X ")
        et_error7.place(x=25, y=35)    
             
    else:
        print("Nombre: "+ alumno_consulta + " -- "+ "Turno: "+lista_alumnos[alumno_consulta][1])            
            
def cerrar_ventana():
    ventana.destroy()
    
ventana=tk.Tk()
ventana.title("Sistema de ingresos de Alumnos")
ventana.config(width=400, height=480)

et_bienvenido=tk.Label(text="Bienvenido!")
et_bienvenido.place(x=170, y=5)

et_menu=tk.Label(text="Utilice la opcion que desee:")
et_menu.place(x=30, y=40)

et_ingreso=tk.Label(text="*Ingresar alumnos:")
et_ingreso.place(x=30, y=70)

et_nombre=tk.Label(text="-Nombre del alumno:")
et_nombre.place(x=40, y=100)

caja_nombre=tk.Entry()
caja_nombre.place(x=45, y=120, width=100, height=25)

et_cursos=tk.Label(text="-Cant. de cursos inscriptos:")
et_cursos.place(x=40, y=150)

caja_cursos=tk.Entry()
caja_cursos.place(x=45, y=170, width=100, height=25)

et_turno=tk.Label(text="-Turno:")
et_turno.place(x=220, y=100)

caja_turno=tk.Entry()
caja_turno.place(x=225, y=120, width=100, height=25)

et_separador1=tk.Label(text="--------------------------")
et_separador1.place(x=222, y=150)


boton_agregar= tk.Button(text="Agregar alumno",command=agregar)
boton_agregar.place(x=240, y=170)


et_separador2=tk.Label(text="------------------------------------------------------------")
et_separador2.place(x=50, y=200)

et_consultas=tk.Label(text="*Consultas:")
et_consultas.place(x=30, y=220)

boton_ver_alumnos= tk.Button(text="Ver lista de alumnos",command=consulta_lista)
boton_ver_alumnos.place(x=140, y=250)

et_consulta_gral=tk.Label(text="-Ingresar nombre del alumno:")
et_consulta_gral.place(x=30, y=290)

caja_ver_gral=tk.Entry()
caja_ver_gral.place(x=70, y=335, width=100, height=25)

boton_ver_turno= tk.Button(text="Ver turno del alumno",command=consulta_turnos)
boton_ver_turno.place(x=200, y=320)

boton_ver_cursos= tk.Button(text="Ver cursos del alumno",command=consulta_cursos)
boton_ver_cursos.place(x=197, y=355)

etiqueta_separador3=tk.Label(text="------------------------------------------------------------")
etiqueta_separador3.place(x=50, y=400)

boton_salir= tk.Button(text="Salir!",command=cerrar_ventana)
boton_salir.place(x=175, y=430)

ventana.mainloop()
