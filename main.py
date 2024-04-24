from datetime import datetime
import click
from src.services.omie_market_price.omie_data_service import OmieDataService
from src.repositories.omie_http_repository import OmieHttpRepository
from src.repositories.mysql_repository import MySqlRepository

@click.command()
@click.option('--country', type=click.Choice(['es', 'pt', 'all']))
@click.option('--start_date', type=click.DateTime(formats=['%Y-%m-%d']), help='start date')
@click.option('--end_date', type=click.DateTime(formats=['%Y-%m-%d']), help='end date')
@click.option('--today', flag_value=True, )
def cli(country, start_date, end_date, today):
    http_repository = OmieHttpRepository()
    mysql_repository = MySqlRepository()
    service = OmieDataService(http_repository, mysql_repository)

    if today:
        service.main(country, datetime.now())
    if start_date and end_date:
        service.main(country, start_date, end_date)
    if start_date and not end_date:
        service.main(country, start_date)


if __name__ == "__main__":
    cli()
