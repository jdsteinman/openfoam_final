%%
clc
clear all
close all

%% Import Data
datA = readtable("meshA.csv");
datB = readtable("meshB.csv");
datC = readtable("meshC.csv");
datD = readtable("meshD.csv");

get_vortex_spacing(datD.arc_length, datD.U_2)


%% Function
function[lambda]=get_vortex_spacing(x, u)
    L=length(x);
    T=x(2)-x(1);
    Fs=1/T;
    
    U = u - mean(u);
    Y = fft(U);
    
    P2 = abs(Y/L);
    P1 = P2(1:L/2+1);
    P1(2:end-1) = 2*P1(2:end-1);
    
    f = Fs*(0:(L/2))/L;
    plot(f,P1) 
    title('Single-Sided Amplitude Spectrum of U_Z for Mesh D')
    xlabel('f (Hz)')
    ylabel('|P1(f)|')
    
    [a,loc]=max(P1);  % oscillations-per-unit-length
    freq = f(loc);
    freq
    lambda = 1/freq;   
    
end