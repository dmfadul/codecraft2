$(document).ready(function(){
    $("#telefone").inputmask("(99) 99999-9999");


    $('#contactForm').on('submit', function(event) {
        event.preventDefault();
        
        
        $('#nomeError').text('');
        $('#telefoneError').text('');
        $('#emailError').text('');
        
        
        const nome = $('#nome').val().trim();
        const telefone = $('#telefone').val().trim();
        const email = $('#email').val().trim();
        const pedido = $('#pedido').val().trim();
        const simChecked = $('#sim').prop('checked');
        const naoChecked = $('#nao').prop('checked');

        let valid = true;
        
        
        if (nome === '') {
            $('#nomeError').text('Por favor, insira seu nome.');
            valid = false;
        }
        
        
        const telefoneRegex = /^\(\d{2}\) \d{5}-\d{4}$/;
        if (!telefoneRegex.test(telefone)) {
            $('#telefoneError').text('Por favor, insira um telefone válido no formato (DD) xxxxx-xxxx.');
            valid = false;
        }
        
       
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            $('#emailError').text('Por favor, insira um e-mail válido.');
            valid = false;
        }

        
        if (!simChecked && !naoChecked) {
            alert('Por favor, confirme se você descreveu o que precisa.');
            valid = false;
        }
        
        if (valid) {
            const dataDict = {
                nome: nome,
                telefone: telefone,
                email: email,
                pedido: pedido,
                confirmado: simChecked ? 'Sim' : 'Não'
            };
            
            sendMessageToServer(dataDict);        
        }
    });

    
    $('#telefone').on('input', function (e) {
        let input = e.target.value;
        input = input.replace(/\D/g, ''); 
        input = input.substring(0, 11); 

        if (input.length > 0) {
            input = '(' + input;
        }
        if (input.length > 3) {
            input = input.slice(0, 3) + ') ' + input.slice(3);
        }
        if (input.length > 10) {
            input = input.slice(0, 10) + '-' + input.slice(10);
        }

        e.target.value = input;
    });
});

