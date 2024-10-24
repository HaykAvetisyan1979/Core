function processFormData() {
    // Access the form
    let form = document.getElementById('myForm');
    //Access the elements by name and get values
    let city = form.elements.city.value;
    let country = form.elements.country.value;
  
    // insertData(city, country);
    table = document.getElementById('dataTable')
    table.elements.addrow();
    table.insertData({'city':city, 'country':country});
      
    document.getElementById('city').value = '';
    document.getElementById('country').value = '';
  };