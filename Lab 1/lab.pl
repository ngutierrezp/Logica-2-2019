% ###########################
% Base de conocimiento
% ###########################


% #####################################################################################
% HECHOS



% colores posibles de una cereza

color("Rosa").
color("Rojo Claro").
color("Rojo").
color("Rojo Oscuro").
color("Caoba").
color("Caoba Oscuro").
color("Negro").

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

% nivel de Durofel

dureza("Extra blando").
dureza("Nlando").
dureza("Rigido").
dureza("Extra rigido").

% Anomalias estructurales de la cereza

anomalia("Decoloracion").
anomalia("Depresion").
anomalia("Machucon").
anomalia("Arrugado").
anomalia("Protuberancia").

% nivel de anomalia

nivel_anomalia("Decoloracion","Bajo").
nivel_anomalia("Decoloracion","Medio").
nivel_anomalia("Decoloracion","Alto").
nivel_anomalia("Decoloracion","Completo").

nivel_anomalia("Depresion","Medio").
nivel_anomalia("Depresion","Alto").
nivel_anomalia("Depresion","Completo").

nivel_anomalia("Machucon","Medio").
nivel_anomalia("Machucon","Alto").
nivel_anomalia("Machucon","Completo").

nivel_anomalia("Arrugado","Alto").
nivel_anomalia("Arrugado","Completo").

nivel_anomalia("Protuberancia","Alto").
nivel_anomalia("Protuberancia","Completo").


% tamaño del pendulo

pendulo(0).

% defectos


% No se si esto está bien del todo, tal vez se puede hacer con solo clausulas pero no se me ocurre
% de que manera puede ser.
defecto("Sin Color","Rosa",_,_,"Brillante",_,"Decoloracion","Bajo",_).    
defecto("Madurez excesivo","negro",_,_,"Opaco","Extra Blando","Decoloracion","Bajo",_).    



% #####################################################################################
% PREDICADO (Clausulas de Horn)

defecto(SALIDA,COLOR,MANCHA,NIVEL_MANCHA,BRILLO,DUREZA,ANOMALIA,NIVEL_ANOMALIA,PENDULO):-
    % Se consulta si lo que se ingresa realmente existe.
    color(COLOR),
    mancha(MANCHA),
    nivel_mancha(NIVEL_MANCHA),
    brillo(BRILLO),
    dureza(DUREZA),
    anomalia(ANOMALIA),
    nivel_anomalia(ANOMALIA,NIVEL_ANOMALIA),
    defecto(SALIDA,COLOR,MANCHA,NIVEL_MANCHA,BRILLO,DUREZA,ANOMALIA,NIVEL_ANOMALIA,PENDULO).



% 8=mm=D---








% http://www.fdf.cl/pdtcerezos/2014/novedades/archivos/Poster_Danos_Cerezos.pdf
%



