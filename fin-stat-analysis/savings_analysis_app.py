"""
@date: 2020-09-27
@author: Jaco Koekemoer
"""
import fin_stat_analysis_oo.account_analyzer as aa
from savings_model import expense_transaction_types, income_transaction_types, prepare_directory

class SavingsAnalysisApp:

    def run(self):
        # Get a list of transaction from the 25th of the previous month to the 24th of the current month as csv
        date = "202008" #Current month
        account_type = "Savings"
        input_filename = "SavingsTransactionHistory" + date
        account_analyzer = aa.AccountAnalyzer(date, account_type, input_filename)
        account_analyzer.set_expense_transaction_types(expense_transaction_types)
        account_analyzer.set_income_transaction_types(income_transaction_types)
        account_analyzer.set_prepare_directory(prepare_directory)
        account_analyzer.analyze()


if __name__ == '__main__':
    savings_analysis_app = SavingsAnalysisApp()
    savings_analysis_app.run()