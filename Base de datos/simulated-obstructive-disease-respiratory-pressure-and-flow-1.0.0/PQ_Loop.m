%% PQ loop plotting COPD data
% Jaimey Clifton
% Last Updated: 27OCT2023

clear
clc
close all

% Inputs ==================================================================

SubjectNumber = 1;
PEEP = 0;
Size = 300;

% Load Data ===============================================================

BOB_infile_format = 'ProcessedCOPD_Subject%02d_%dcmH2O_%dmL.mat';
BOB_infile = sprintf(BOB_infile_format, SubjectNumber, PEEP, Size);

load(BOB_infile)

% BOB_Infile:
% 'T' - time [s]
% 'P' - Gauge pressure reading [cmH2O]
% 'Q' - Flow [L/s]
% 'V' - Volume [L]
% 'Ind' - Inspiratory indices

% Plot PQ loop (1 breath) =================================================
figure(1)
hold on 
plot(smooth(P(Ind(1):Ind(2))),smooth(Q(Ind(1):Ind(2))))
grid minor
yline(0)
xline(0)
xlabel('Pressure [cmH20]')
ylabel('Flow [L/s]')
hold off

saveas(figure(1), 'figure_1.png')
close(figure(1))
clear all