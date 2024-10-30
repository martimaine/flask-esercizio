Progettare e sviluppare un semplice applicazione web per gestire l'iscrizione di una maratona, questa dovrà contenere almeno tre pagine:
- Una pagina dove verrà visualizzata la lista tutti i partecipanti (id, Nome, Cognome) 
- Una pagina di dettaglio dove per ogni utente visualizzeremo  ID, Nome, Cognome e Email
- Un form di iscrizione per un nuovo partecipante (con Nome, Cognome e Email)
L'id sarà considerato anche come numero di gara e della pettorina dell'utente.

Altri requisiti:
I campi del form dovranno essere validati lato client con javascript.
I dati dovranno essere gestiti attraverso un database (Es: Mariadb) e query SQL
Il backend dovrà utilizzare il framework flask ed implementare le rotte necessarie (in stile REST).
Si consiglia di servire le pagine con flask (e template JINJA) 

E' possibile utilizzare bootstrap e altre librerie python (tipo sqlalchemy), documentazione online e consultare gli esercizi visti a lezione.
La struttura e progettazione del servizio sono libere.

Bonus:
- Dopo aver inviato il form di iscrizione, indicare all'utente il proprio id/numero maglia
- Usando "preventDefault()" e un action listener e una fetch fare in modo che il form non porti ad un'altra pagina ma che si comporti come una single page application, per far questo sarà necessario eventualmente implementare altre rotte.
