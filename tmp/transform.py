from data_transform import order2order
import click

@click.command()
@click.option('--filepath', type=click.STRING, required=True, help='input excel file path typing plz')
@click.option('--filename', type=click.STRING, required=False, default="generated_excelfile.xlsx", help='new generated excel file name typing plz')

def main(filepath, filename):
    order_df = order2order(filepath)
    order_df.to_excel(filename)

if __name__ == '__main__':
    main()