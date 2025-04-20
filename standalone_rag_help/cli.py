import click
import sys
from .rag_core import Help, install_dependencies_if_needed

@click.command()
@click.argument('question', required=False, default=None)
def main(question):
    """
    Query the documentation using RAG.
    If QUESTION is provided, asks it directly.
    Otherwise, enters an interactive loop.
    """
    if not install_dependencies_if_needed():
        click.echo("Required dependencies could not be installed. Please install them manually.", err=True)
        click.echo("You might need: pip install llama-index-core llama-index-embeddings-huggingface torch sentence-transformers", err=True)
        sys.exit(1)

    try:
        rag_helper = Help()
    except Exception as e:
        click.echo(f"Error initializing RAG helper: {e}", err=True)
        click.echo("Please ensure dependencies are installed and models can be downloaded.", err=True)
        sys.exit(1)

    if question:
        try:
            context = rag_helper.ask(question)
            click.echo(context)
        except Exception as e:
            click.echo(f"Error processing question: {e}", err=True)
            sys.exit(1)
    else:
        click.echo("Entering interactive mode. Ask questions about the documentation.")
        click.echo("Type 'exit' or 'quit' to leave.")
        while True:
            try:
                user_input = click.prompt("?>", prompt_suffix=' ')
                if user_input.lower() in ['exit', 'quit']:
                    break
                context = rag_helper.ask(user_input)
                click.echo(context)
            except click.exceptions.Abort:
                # Handle Ctrl+C or Ctrl+D gracefully
                break
            except EOFError:
                break
            except Exception as e:
                click.echo(f"Error: {e}", err=True)
        click.echo("\nExiting.")

if __name__ == '__main__':
    main()
