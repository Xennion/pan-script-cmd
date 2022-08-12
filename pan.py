from netmiko import ConnectHandler
import click


@click.command()
@click.help_option("-h", "--help")
@click.argument("host", type=str)
@click.argument("file", type=click.Path(exists=True))
@click.option("-u", "--username", type=str, prompt=True)
@click.option("-p", "--password", type=str, prompt=True, hide_input=True)
def run(host: str, file: str, username: str, password: str, diff: bool):
    """Sends a config FILE to a pan-os HOST with netmiko

    \b
    HOST is the hostname or IP address of the device
    FILE is the path to the config file to send
    """

    client = ConnectHandler(
        host=host,
        username=username,
        password=password,
        device_type="paloalto_panos",
    )

    print(client.config_mode())
    print(client.send_config_from_file(file))
    print(client.exit_config_mode())


if __name__ == "__main__":
    run()
