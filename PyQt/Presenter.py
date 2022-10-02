class MainPresenter(object):

    def __init__(self, view, data_model, colour_list):
        self.view = view

        self.data_model = data_model

        self.presenter = Presenter(self.view.getOptionView(), colour_list)
        self.plot_presenter = PlotPresenter(self.view.getPlotView())
        # connect statements
        self.view.getOptionView().plotSignal.connect(self.updatePlot)

    # handle signals
    def updatePlot(self):
        # only care about the colour if the button is pressed
        colour, freq, phi = self.presenter.getPlotInfo()
        grid_lines = self.presenter.getGridLines()

        self.data_model.genData(freq, phi)
        x_data = self.data_model.getXData()
        y_data = self.data_model.getYData()

        self.plot_presenter.plot(x_data, y_data, grid_lines, colour)

class PlotPresenter(object):

    def __init__(self, view):
        self.view = view

    def plot(self, x_data, y_data, grid_lines, colour_code):
        self.view.addData(x_data, y_data, grid_lines, colour_code, "x")


class Presenter(object):

    def __init__(self, view, colours):
        self.view = view
        self.view.setColours(colours)

    def getPlotInfo(self):
        return str(self.view.getColour()), self.view.getFreq(), self.view.getPhase()

    def getGridLines(self):
        return self.view.getGridLines()
