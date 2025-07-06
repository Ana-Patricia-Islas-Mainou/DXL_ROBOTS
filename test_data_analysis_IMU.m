%%
% IMU 

T_imu = readtable('LOGS\FLAT\MPU6050_FLAT_TEST1.csv','ReadVariableNames',false);
T_imu = rmmissing(T_imu);
A_imu = table2array(T_imu);

basicStadistics(A_imu)
makePlots(A_imu)

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
    colNames = {'ax','ay','az','gx', 'gy', 'gz', ...
    'ax_calib', 'ay_calib', 'az_calib'};
    
    % Crear tabla
    T = array2table(M, ...
        'VariableNames', colNames, ...
        'RowNames', rowNames);
       
    disp(T)
end

function makePlots(matrix)
    y_labels ={'ax [$\frac{m}{s}$]','ay [$\frac{m}{s}$]', ...
        'az [$\frac{m}{s}$]','gx [$deg$]', ...
        'gy [$deg$]', 'gz [$deg$]', ...
        'ax calib [$\frac{m}{s}$]', 'ay calib[$\frac{m}{s}$]', ...
        'az calib [$\frac{m}{s}$]'};
    for i = 2:10
        figure 
        plot(matrix(:,1),matrix(:,i))
        set(gca,"TickLabelInterpreter",'latex')
        %title(tit)
        ylabel(y_labels(i-1),'interpreter','latex')
        xlabel("t [s]",'interpreter','latex')
        pbaspect([1,1,1])
        grid on
    end 
end 