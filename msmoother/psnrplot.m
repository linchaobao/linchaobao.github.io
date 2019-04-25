clear; close all;
load 'psnrdatamat.mat';
num_of_imgs = 8;

sig_ind = 1; %1,2,3,4 

for loss_func = 1:5
    onesig_dataall = img1(sig_ind:4:end,:);
    onesig_dataall = [onesig_dataall; img2(sig_ind:4:end,:)];
    onesig_dataall = [onesig_dataall; img3(sig_ind:4:end,:)];
    onesig_dataall = [onesig_dataall; img4(sig_ind:4:end,:)];
    onesig_dataall = [onesig_dataall; img5(sig_ind:4:end,:)];
    onesig_dataall = [onesig_dataall; img6(sig_ind:4:end,:)];
    onesig_dataall = [onesig_dataall; img7(sig_ind:4:end,:)];
    onesig_dataall = [onesig_dataall; img8(sig_ind:4:end,:)];

    onelossfunc_dataall = [];
    for i = loss_func:5:(5*num_of_imgs)
        st = ((i-1)*16)+1;
        ed = (i*16);
        onelossfunc_dataall = [onelossfunc_dataall; onesig_dataall(st:ed,:)];
    end

    x_labels = [1 2 3 4 5];
    colors = {[0,0.8,0],[0.6,0.3,1],[1,0,0],[0.6,0,0.3],[0.3,0.4,0],[0,0.3,0.7],[0.4,0.5,1]}; %'rgbcmy';
    linetype = {'-*','--v','-o', '-s'}; %'rgbcmy';

    figure1 = figure;
    % Create axes
    axes1 = axes('Parent',figure1,'XTickLabel',{'8','16','32','64','128'},...
        'XTick',[1 2 3 4 5]);

    ylim(axes1,[28 52]);
    box(axes1,'on');

    hold on;
    for ft = 1:4 %filter type
        onefilter_data = onelossfunc_dataall(ft:4:end,:);
        mean_psnr = mean(onefilter_data,1);
        max_psnr = max(onefilter_data); upper_dist=max_psnr-mean_psnr;
        min_psnr = min(onefilter_data); lower_dist=mean_psnr-min_psnr;
        plot(x_labels,mean_psnr, linetype{ft}, 'Color', colors{ft}, 'LineWidth', 2); hold on;
    end

    % Create xlabel
    xlabel('\it n \rm[log scale]');

    % Create ylabel
    ylabel('PSNR (dB)');

    legend1 = legend('box','Gaussian','bilateral','guided');
    set(legend1,'Position',[0.5957 0.1659 0.2857 0.2937]);

    set(legend1,'FontSize',18);
    set(get(gca,'XLabel'),'FontSize',18);
    set(get(gca,'YLabel'),'FontSize',18);
    set(gca,'FontSize',18)

    annotation(figure1,'line',[0.1359 0.9062],[0.5293 0.5303],'LineStyle',':',...
    'Color',[0.502 0.502 0.502]);
end



