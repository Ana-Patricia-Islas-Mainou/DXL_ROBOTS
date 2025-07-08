%% DATA ANALYSIS
clear; clc

showPlots = 0;
% basic analisis of all samples
[T_c1_FLAT, A_c1_FLAT, stats_c1_FLAT] = basicAnalysis('LOGS\FLAT\TEST4_CURRENT.csv',1,showPlots);
[T_v1_FLAT, A_v1_FLAT, stats_v1_FLAT] = basicAnalysis('LOGS\FLAT\TEST4_VOLTAGE.csv',2,showPlots);
[T_t1_FLAT, A_t1_FLAT, stats_t1_FLAT] = basicAnalysis('LOGS\FLAT\TEST4_TEMPERATURE.csv',3,showPlots);
[T_s1_FLAT, A_s1_FLAT, stats_s1_FLAT] = basicAnalysis('LOGS\FLAT\TEST4_SPEED.csv',4,showPlots);

% current specific
make_lineplot_all_motors(A_c1_FLAT, "Current [mA]")
%make_lineplot_individual_run(A_c1_FLAT,"Current [mA]", 18)
make_lineplot_compareLegs(A_c1_FLAT,"Current [mA]")
make_lineplot_wholeRobot(A_c1_FLAT,"Current [mA]")

% voltage specific -------
%make_lineplot_all_motors(A_v1_FLAT, "Voltage [V]")

% temperature specific ---------
%make_lineplot_all_motors(A_t1_FLAT,"Temperature [°C]")

% speed specific ----
%make_boxplot_individual_run(A_s1_FLAT)
%make_lineplot_all_motors(A_s1_FLAT, "Speed [$/frac{rad}{s}$]")

%clc;
showPlots = 1;

% power and energy ---------
%[eP, ePTot, eE, eETot] = electPowerEnegry(A_c1_FLAT, A_v1_FLAT, 0.1, showPlots);

%T_eP1_FLAT = basicStadistics(eP);
%T_eE1_FLAT = basicStadistics(eE);

%make_boxplot_individual_run(eP,"Electrical Power [W]");
%make_boxplot_individual_run(eE,"Electrical Energy [J]");

% KPI ----------------------------------
% COST OF TRANSPORT ------
%costOfTransport(5.2, 9.81, 1.11, eETot) % mRobot, g, d, eETot

%% FUNCIONES 

% CALCULAR POTENCIA ELECTRICA Y ENERGIA -----------------------------------
function [eP, ePTot, eE, eETot] = electPowerEnegry(I_matrix, V_matrix, dt, ...
    showPlots)
    eP = I_matrix; eE = I_matrix;
    eP(:,2:end) = abs(I_matrix(:,2:end).*0.001) .* V_matrix(:,2:end);
    ePTot = sum(eP, "all")

    eE(:,2:end) = eP(:,2:end) .*dt;
    eETot = sum(eE,"all")

    if showPlots
        make_lineplot_all_motors(eP,"Electrical Power")
        make_lineplot_all_motors(eE, "Electrical Energy")

        make_lineplot_wholeRobot(eP,"Electrical Power")
        make_lineplot_wholeRobot(eE,"Electrical Energy")
    end
end

function Ect = costOfTransport(mRobot, g, d, eETot)
    Ect = (eETot)/(mRobot*g*d);
end

% GRAFICAS DE TODOS LOS MOTORES JUNTOS (PRUEBA) ---------------------------
function make_lineplot_all_motors(matrix, tit)
    figure 
    hold on
    for i = 2:13
        plot(matrix(:,1),matrix(:,i))
    end 
    legend('7','8','9','10','11','12','13','14','15','16','17',...
        '18','Interpreter','latex')
    set(gca,"TickLabelInterpreter",'latex')
    title(tit)
    pbaspect([1,1,1])
    grid on
    hold off
end 

function make_lineplot_compareLegs(matrix, dataInfo)
    for i = 2:2:12
        figure 
        hold on
        plot(matrix(:,1),matrix(:,i))
        plot(matrix(:,1),matrix(:,i+1))
        legend(int2str(i+5),int2str(i+6),'Interpreter','latex')
        xlabel('t[s]','interpreter','latex')
        ylabel(dataInfo,'interpreter','latex')
        set(gca,"TickLabelInterpreter",'latex')
        pbaspect([1,1,1])
        grid on
        hold off
    end 
end 

function make_lineplot_wholeRobot(matrix, dataInfo)
    data = sum(matrix(:,2:end),2);
    figure 
    plot(matrix(:,1),data)
    xlabel('t[s]','interpreter','latex')
    ylabel(dataInfo,'interpreter','latex')
    set(gca,"TickLabelInterpreter",'latex')
    pbaspect([1,1,1])
    grid on
    hold off
end
% GRAFICAS INDIVIDUALES (PRUEBA) ------------------------------------------
function make_boxplot_individual_run(matrix, dataInfo) % box - ID completo
    figure 
    boxchart(matrix(:,2:end))
    grid on
    xticklabels({'7','8','9','10','11','12','13','14','15','16','17','18'})
    xlabel('Motor ID','interpreter','latex')
    ylabel(dataInfo,'interpreter','latex')
    set(gca,"TickLabelInterpreter",'latex')
    pbaspect([1,1,1])
end

function make_lineplot_individual_run(matrix, dataInfo, ID) % line - 1 ID
    figure 
    id_index = ID - 5;
    plot(matrix(:,1),matrix(:,id_index))
    grid on
    xticklabels({'7','8','9','10','11','12','13','14','15','16','17','18'})
    x = 'Motor ID '+int2str(ID);
    xlabel(x,'interpreter','latex')
    ylabel(dataInfo,'interpreter','latex')
    pbaspect([1,1,1])
    set(gca,"TickLabelInterpreter",'latex')
end


% CARGA Y LIMPIEZA DEL ARCHIVO --------------------------------------------
function T = loadAndCleanData(fname)
    T = readtable(fname,'ReadVariableNames',false);
    T= rmmissing(T);
    T = T(:,1:end-1);
    % [numFilas, numColumnas] = size(T);
    % for i = 1:numFilas
    %     for j = 1:numColumnas
    %         T(i,j)
    %         T(i,j) = str2num(T(i,j))
    %     end
    % end
    
end


% OBTENER ESTADISTICA BASICA ----------------------------------------------
function T = basicStadistics(A)
    d1 = mean(A(:,2:end));
    d2 = min(A(:,2:end));
    d3 = max(A(:,2:end));
    d4 = range(A(:,2:end));
    d5 = std(A(:,2:end));
    d6 = var(A(:,2:end));
    
    M = [d1; d2; d3; d4; d5; d6];

    % Nombres de filas
    rowNames = {'mean','min','max','range','std','var'};
    colNames = {'ID 7','ID 8','ID 9','ID 10', 'ID 11', 'ID 12', ...
    'ID 13', 'ID 14', 'ID 15', 'ID 16', 'ID 17', 'ID 18'};
    
    % Crear tabla
    T = array2table(M, ...
        'VariableNames', colNames, ...
        'RowNames', rowNames);
       
    disp(T)
end

% BASICOS PARA CADA ARCIVO ------------------------------------------------
function [T,A, stats_T] = basicAnalysis(fname, id, showPlots)
    T = loadAndCleanData(fname)
    if id == 1
        dataInfo = "Current [mA]"; 
        [T, A] = bits2mAmp(T);
    elseif id == 2
        dataInfo = "Voltage [V]"; 
        [T, A] = bits2volts(T);
    elseif id == 3 
        dataInfo = "Temperature [$^\circ$C]"; 
        [T, A] = bits2temp(T);
    elseif id == 4 
        dataInfo = "Speed [$\frac{rad}{s}$]"; 
        [T, A] = bits2radsec(T);
    else 
        return
    end
    
    %[T, A] = bits2mAmp(T); % bits to mAmpares

    stats_T = basicStadistics(A); % basic stats

    if showPlots
        make_boxplot_individual_run(A, dataInfo)
    end

    %make_lineplot_individual_run(matrix, dataInfo, ID)
    %make_lineplot_individual_run(A, dataInfo, ID)
end

% CONVERSIONES DE BITS A DATOS UTILES -------------------------------------
function [T,A] = bits2mAmp(T)
    T(:,2:end) = T(:,2:end).*3.36;
    A = table2array(T);
end 

function [T,A] = bits2volts(T)
    T(:,2:end) = T(:,2:end).*0.1;
    A = table2array(T);
end 

function [T,A] = bits2temp(T)
    T(:,2:end) = T(:,2:end).*1;
    A = table2array(T);
end 

function [T,A] = bits2radsec(T)
    T(:,2:end) = T(:,2:end).* 0.229 .* 0.1047;
    A = table2array(T);
end 