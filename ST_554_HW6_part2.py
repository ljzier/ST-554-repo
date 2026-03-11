# creating a slope simulator class

class SLR_slope_simulator:
    # initializing
    def __init__(self, beta_0, beta_1, x, sigma, seed):
        self.beta_0 = beta_0
        self.beta_1 = beta_1
        self.sigma = sigma
        self.x = x
        self.n = len(x)
        self.rng = default_rng(seed)
        self.slopes = []

    # generate one dataset
    def generate_data(self):
        #create the 'responses' modeled from the line plus a random deviation
        y=self.beta_0 + self.beta_1*self.x + self.rng.standard_normal(self.n)
        return self.x, y

    # fit the SLR model and return slope
    def fit_slope(self, x, y):
        reg = linear_model.LinearRegression()
        fit=reg.fit(x.reshape(-1, 1), y)
        return fit.coef_[0]

    #take in n_sims and run the above 2
    def run_simulations(self, n_sims):
        for i in range(n_sims):
            x, y = self.generate_data()
            slope = self.fit_slope(x, y)
            self.slopes.append(slope)
        self.slopes = np.array(self.slopes) #convert to np array

    # produce histogram of slopes
    def plot_sampling_distribution(self):
        if len(self.slopes) == 0:
            print("run_simulations() must be called first")
            return
        plt.hist(self.slopes)
        plt.show()

    # find probability
    def find_prob(self, value, sided):
        if len(self.slopes) == 0:
            print("run_simulations() must be called first")
            return
        if sided == "above":
            prob = self.slopes[:,1] > value
            return prob.mean()
        if sided == "below":
            prob = self.slopes[:,1] < value
            return prob.mean()
        if sided == "two-sided":
            if value > self.x.median():
                prob = (self.slopes[:,1] > value)
                return 2*prob.mean()
            if value <= self.x.median():
                prob = (self.slopes[:,1] < value)
                return 2*prob.mean()
