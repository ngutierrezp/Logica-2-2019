% ###########################
% Base de conocimiento
% ###########################


% #####################################################################################
% HECHOS


% Colores posibles de una cereza

color("Rosa",1).
color("Rojo Claro",2).
color("Rojo",2).
color("Rojo Oscuro",2).
color("Caoba",2).
color("Caoba Oscuro",2).
color("Negro",3).

% Tipos de Manchas

mancha("Quemadura").
mancha("Cicatriz").

% Niveles de Manchas

nivel_mancha("Quemadura","Medio").
nivel_mancha("Quemadura","Alto").
nivel_mancha("Quemadura","Completo").

nivel_mancha("Cicatriz","Medio").
nivel_mancha("Cicatriz","Alto").
nivel_mancha("Cicatriz","Completo").

% Brillo

brillo("Opaco").
brillo("Brillante").

% Nivel de Durofel (firmeza)

dureza("Extra blando").
dureza("Blando").
dureza("Rigido").
dureza("Extra rigido").

% Anomalias estructurales de la cereza

anomalia("Decoloracion").
anomalia("Depresion").
anomalia("Machucon").
anomalia("Arrugado").
anomalia("Protuberancia").

% Nivel de anomalia

nivel_anomalia("Decoloracion","Bajo").
nivel_anomalia("Decoloracion","Medio").
nivel_anomalia("Decoloracion","Alto").
nivel_anomalia("Decoloracion","Completo").

nivel_anomalia("Depresion","Bajo").
nivel_anomalia("Depresion","Medio").
nivel_anomalia("Depresion","Alto").
nivel_anomalia("Depresion","Completo").

nivel_anomalia("Machucon","Bajo").
nivel_anomalia("Machucon","Medio").
nivel_anomalia("Machucon","Alto").
nivel_anomalia("Machucon","Completo").

nivel_anomalia("Arrugado","Bajo").
nivel_anomalia("Arrugado","Medio").
nivel_anomalia("Arrugado","Alto").
nivel_anomalia("Arrugado","Completo").

nivel_anomalia("Protuberancia","Bajo").
nivel_anomalia("Protuberancia","Medio").
nivel_anomalia("Protuberancia","Alto").
nivel_anomalia("Protuberancia","Completo").


% Existencia del pedunculo

pedunculo(0).
pedunculo(1).

% Defectos

% Un defecto se puede definir como: 
% defecto(SALIDA,NUM,MANCHA,NIVEL_MANCHA,BRILLO,DUREZA,ANOMALIA,NIVEL_ANOMALIA,PEDUNCULO).

%       SALIDA: Corresponde al nombre del defecto, es solo un valor de retorno.

%       NUM: Corresponde a un valor de color, esto viene dado por la función de validar datos,
%           si existe el color puesto, se le da un valor numero.

%       MANCHA: Corresponde a la mancha presente en la fruta

%       NIVEL_MANCHA: Corresponde al nivel de mancha presente en la fruta.

%       BRILLO: Corresponde al brillo de la fruta.

%       DUREZA: Corresponde a la dureza de la fruta.

%       ANOMALIA: Corresponde a la anomalia estructural presente en la fruta.

%       NIVEL_ANOMALIA: Corresponde al nivel de anomalia estructuras.

%       PEDUNCULO: Corresponde a si la cereza tiene pedunculo o no. 


% Algunas de las caracteristicas para ciertos defectos, no importan ya que estas caracteristicas
% no aportan ningun valor en la elección del defecto.

defecto("Madurez excesivo",3,_,_,"Opaco","Extra blando","Decoloracion","Bajo",1).
defecto("Sin color",1,_,_,"Brillante",_,"Decoloracion","Bajo",1).
defecto("Magulladura", 2, _, _, _, "Blando", "Machucon", "Medio", 1).
defecto("Fruto arrugado", 2, _, _,"Opaco","Blando","Arrugado","Completo",1).
defecto("Pitting", 2,_,_,_,"Blando","Depresion","Alto",1).
defecto("Fruto gemelo",2,_,_,_,_,"Protuberancia","Alto",1).
defecto("Fruto doble",2,_,_,_,_,"Protuberancia","Alto",1).
defecto("Quemadura solar",2,"Quemadura","Alto","Opaco","Rigido","Decoloracion","Medio",1).
defecto("Cicatriz",2,"Cicatriz","Medio",_,"Rigido",_,_,1).
defecto("Sin pedunculo",2,_,_,_,_,_,_,0).
defecto("Media luna",2,"Cicatriz","Medio",_,_,_,_,1).



% #####################################################################################
% PREDICADO (Clausulas de Horn)


% Esta clausula solo valida que todo lo entregado por el usuario existe.  

validarDatos(COLOR,MANCHA,NIVEL_MANCHA,BRILLO,DUREZA,ANOMALIA,NIVEL_ANOMALIA,PEDUNCULO):-
    color(COLOR, _),
    mancha(MANCHA),
    nivel_mancha(MANCHA,NIVEL_MANCHA),
    brillo(BRILLO),
    dureza(DUREZA),
    anomalia(ANOMALIA),
    nivel_anomalia(ANOMALIA,NIVEL_ANOMALIA),
    pedunculo(PEDUNCULO),!.

% Genera una listas con todos los defectos dadas las caracteristicas de un fruto.
% Puede darse el caso que una caracteristica este presente en varios defectos.

grupoDefectos(SALIDA,COLOR,MANCHA,NIVEL_MANCHA,BRILLO,DUREZA,ANOMALIA,NIVEL_ANOMALIA,PEDUNCULO):-
    findall(SALIDA, defecto(SALIDA,NUM,MANCHA,NIVEL_MANCHA,BRILLO,DUREZA,ANOMALIA,NIVEL_ANOMALIA,PEDUNCULO), SALIDA),
    color(COLOR, NUM),
    validarDatos(COLOR,MANCHA,NIVEL_MANCHA,BRILLO,DUREZA,ANOMALIA,NIVEL_ANOMALIA,PEDUNCULO),!.





% #############################
% # Consulta para Exportacion #
% #############################

% Un fruto de exportación es aquel que tiene:

%           CALIBRE > 24    -> Asumimos que un calibre mayor sigue siendo exportable ya que podemos ver 
%                               frutos grandes en tiendas.

% Y posee defectos apenas visibles:

%           - "Quemadura Solar"
%           - "Magulladura"

% Puede que una cereza tenga uno, ninguno o ambos. 


salida("Exportable",CALIBRE,[]):-
    CALIBRE > 24,
    !.

salida("Exportable",CALIBRE,[L|Ls]):-
    CALIBRE > 24,
    L == "Quemadura solar",
    salida("Exportable",CALIBRE,Ls),
    !.

salida("Exportable",CALIBRE,[L|Ls]):-
    CALIBRE > 24,
    L == "Magulladura",
    salida("Exportable",CALIBRE,Ls),
    !.




% #################################
% # Consulta para Mercado Interno #
% ################################# 


% Un fruto de Mercado Interno es aquel que tiene un calibre medio:
% un calibre medio bajo:

%           CALIBRE <= 24    y
%           CALIBRE >= 22    

% O posee defectos aceptables:

%           - "Quemadura Solar"
%           - "Magulladura"
%           - "Media luna"
%           - "Pitting"
%           - "Sin pedunculo"
%           - "Fruto doble"

% Tambien podemos aceptar cerezas en mercado internos si poseen defectos aceptables 
% y con un calibre superior a 24.



salida("Mercado interno",CALIBRE,[]):-
    CALIBRE >= 22,
    !.

salida("Mercado interno",CALIBRE,[L|Ls]):-
    CALIBRE =< 24,
    CALIBRE >= 22,
    L == "Quemadura solar",
    salida("Mercado interno",CALIBRE,Ls),
    !.

salida("Mercado interno",CALIBRE,[L|Ls]):-
    CALIBRE =< 24,
    CALIBRE >= 22,
    L == "Media luna",
    salida("Mercado interno",CALIBRE,Ls),
    !.
salida("Mercado interno",CALIBRE,[L|Ls]):-
    CALIBRE =< 24,
    CALIBRE >= 22,
    L == "Pitting",
    salida("Mercado interno",CALIBRE,Ls),
    !.
salida("Mercado interno",CALIBRE,[L|Ls]):-
    CALIBRE =< 24,
    CALIBRE >= 22,
    L == "Magulladura",
    salida("Mercado interno",CALIBRE,Ls),
    !.
salida("Mercado interno",CALIBRE,[L|Ls]):-
    CALIBRE =< 24,
    CALIBRE >= 22,
    L == "Sin pedunculo",
    salida("Mercado interno",CALIBRE,Ls),
    !.
salida("Mercado interno",CALIBRE,[L|Ls]):-
    CALIBRE =< 24,
    CALIBRE >= 22,
    L == "Fruto doble",
    salida("Mercado interno",CALIBRE,Ls),
    !.

salida("Mercado interno",CALIBRE,[L|Ls]):-
    CALIBRE >= 22,
    L == "Quemadura solar",
    salida("Mercado interno",CALIBRE,Ls),
    !.
salida("Mercado interno",CALIBRE,[L|Ls]):-
    CALIBRE >= 22,
    L == "Media luna",
    salida("Mercado interno",CALIBRE,Ls),
    !.
salida("Mercado interno",CALIBRE,[L|Ls]):-
    CALIBRE >= 22,
    L == "Pitting",
    salida("Mercado interno",CALIBRE,Ls),
    !.
salida("Mercado interno",CALIBRE,[L|Ls]):-
    CALIBRE >= 22,
    L == "Magulladura",
    salida("Mercado interno",CALIBRE,Ls),
    !.
salida("Mercado interno",CALIBRE,[L|Ls]):-
    CALIBRE >= 22,
    L == "Sin pedunculo",
    salida("Mercado interno",CALIBRE,Ls),
    !.
salida("Mercado interno",CALIBRE,[L|Ls]):-
    CALIBRE >= 22,
    L == "Fruto doble",
    salida("Mercado interno",CALIBRE,Ls),
    !.


% ##########################
% # Consulta para desechar #
% ##########################


% Un fruto de Mercado Interno es aquel que tiene un calibre menor a 22:

%           CALIBRE < 22    

% O/Y posee defectos aceptables:

%           - "Cicatriz"
%           - "Sin color"
%           - "Madurez excesivo"
%           - "Fruto arrugado"
%           - "Fruto gemelo"


salida("Desecho",_,[]):-
    !.

salida("Desecho",C,_):-
    C < 22,
    !.

salida("Desecho",C,[L|Ls]):-
    C > 0,
    L == "Cicatriz",
    salida(_,C,Ls),
    !.
salida("Desecho",C,[L|Ls]):-
    C > 0,
    L == "Sin color",
    salida(_,C,Ls),
    !.
salida("Desecho",C,[L|Ls]):-
    C > 0,
    L == "Madurez excesivo",
    salida(_,C,Ls),
    !.
salida("Desecho",C,[L|Ls]):-
    C > 0,
    L == "Fruto arrugado",
    salida(_,C,Ls),
    !.
salida("Desecho",C,[L|Ls]):-
    C > 0,
    L == "Fruto gemelo",
    salida(_,C,Ls),
    !.
salida("Desecho",C,[L|Ls]):-
    C > 0,
    L == "Fruto doble",
    salida(_,C,Ls),
    !.
salida("Desecho",C,[L|Ls]):-
    C > 0,
    L == "Sin pedunculo",
    salida(_,C,Ls),
    !.
salida("Desecho",C,[L|Ls]):-
    C > 0,
    L == "Pitting",
    salida(_,C,Ls),
    !.
salida("Desecho",C,[L|Ls]):-
    C > 0,
    L == "Media luna",
    salida(_,C,Ls),
    !.
salida("Desecho",C,[L|Ls]):-
    C > 0,
    L == "Magulladura",
    salida(_,C,Ls),
    !.
salida("Desecho",C,[L|Ls]):-
    C > 0,
    L == "Machucon",
    salida(_,C,Ls),
    !.
salida("Desecho",C,[L|Ls]):-
    C > 0,
    L == "Quemadura solar",
    salida(_,C,Ls),
    !.


%##########################################################
% ENTRADA DE CEREZA

% Una cereza la podemos definir como un calibre y muchas caracteristicas asociadas a una propia cereza.
%
% Cereza:
%      -> Calibre (obligatorio)
%      -> Color
%      -> Mancha
%      -> Nivel de mancha
%      -> Brillo
%      -> Dureza
%      -> Anomalia
%      -> Nivel de Anomalia
%      -> Pendulo

% Para una consulta no es necesario que todas estas caracteristicas esten presentes, exepto por el calibre,
% ya que es necesario que una cereza exista con un calibre especifico.


% La clausula tiene:

%       DEFECTOS: corresponde a una lista con todos los defectos selecionados dadas las caracteristicas.
%                -> Es una salida (respuesta).


%       LINEA_EMBALAJE: corresponde a una respuesta dependiento del calibre y los defectos, nos dice, si una
%                       cereza es:
%                               - "Exportable"
%                               - "Mercado interno"
%                               - "Desecho"


%       Valores propios de las cerezas, :
%       -> COLOR
%       -> MANCHA
%       -> NIVEL_MANCHA
%       -> BRILLO
%       -> DUREZA
%       -> ANOMALIA
%       -> NIVEL_ANOMALIA
%       -> PEDUNCULO            

cereza(DEFECTOS,LINEA_EMBALAJE,CALIBRE,COLOR,MANCHA,NIVEL_MANCHA,BRILLO,DUREZA,ANOMALIA,NIVEL_ANOMALIA,PEDUNCULO):-
    grupoDefectos(DEFECTOS,COLOR,MANCHA,NIVEL_MANCHA,BRILLO,DUREZA,ANOMALIA,NIVEL_ANOMALIA,PEDUNCULO),
    salida(LINEA_EMBALAJE,CALIBRE,DEFECTOS).
