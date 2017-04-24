var opt_values = [];
$('#productname option').each(function(){
 opt_values.push($(this).text());
});
var cc = opt_values.length;
var i = 2;
var k = '<select  id="productname" name="productname" onchange="pricechange()"></select>';
var Invoice = {
  symbol: '€',
  init: function() {
    Invoice.update();
    Invoice.uiEvent();
  },
  uiEvent: function() {

    $('#items').on('click', '.delete', function(e) {
      e.preventDefault();
      $(this).parent().parent().remove();
      Invoice.update();
    });

    $('#items').on('change', '.price,.quantity,.tax_rate', function(e) {
      Invoice.update();
    });

    $('#addItemButton').on('click', function(e) {
      e.preventDefault();
      Invoice.addItem();
      Invoice.update();
    });
  },
  update: function() {
    var subtotal = 0,
      taxable = 0,
      taxs = {},
      total = 0,
      productc = 0;


    $('#items tr').each(function() {
      //$(this).css('background','#f00');

      var price = parseFloat($('.price', this).val());
      var qta = parseInt($('.quantity', this).val());
      var tax_rate = parseInt($('.tax_rate option:selected', this).val());

      var total_price = price * qta;
      subtotal += total_price;
      productc = productc +1;

      if (tax_rate > 0) {
        var tax = (total_price * tax_rate) / 100;

        var tax_rate_item = taxs[tax_rate] || 0;
        taxs[tax_rate] = tax_rate_item + tax;
        taxable += tax;
      }
      $('.price', this).val(parseFloat(price).toFixed(2));
      $('.total-price', this).html('€ ' + parseFloat(total_price).toFixed(2));
    });

    $('#invoiceSubtotal').html('€ ' + parseFloat(subtotal).toFixed(2));

    $('#invoiceTax').html('€ ' + parseFloat(taxable).toFixed(2));
      $('#productcount').attr("value",productc);
    total = parseFloat(subtotal) + parseFloat(taxable);
    $('#invoiceTotal').html('€ ' + parseFloat(total).toFixed(2));
      $("#invoiceTotal").attr("value",total);

    //$('#taxs').hide();
    $('#taxs tbody tr').remove();

    $.each(taxs, function(index, value) {
      var parse_value = parseFloat(value).toFixed(2)
      $('#taxs tbody').append('<tr><th>' + index + '%</th><td>€ ' + parse_value + '</td></tr>');
    });
    Invoice.displayTaxs();
    Invoice.displayDelete();
  },
  addItem: function() {
      c = "desc"+i;
      d = "price"+i;
      e = "quantity"+i;
    var html = '<tr id="item-'+i+'"><td>'+k+'</td><td><input type="number" class="price" name="'+d+'" step="0.01" value="0.00"></td><td><input type="number" class="quantity" name="'+e+'" step="1" value="0"></td><td><select name="tax" id="" class="tax_rate"><option value="">None</option><option value="21">IVA 21%</option><option value="14">IVA 14%</option></select></td><td class="total-price">€ 0,00</td><td><a href="#" class="delete">x</a></td></tr>';
    $('#items').append(html);
    for(p=0 ; p < opt_values.length ; p++)
    {
        var dd = opt_values[p];
        var ppp = '#item-'+i +' select#productname';
        $(ppp).append('<option value ="'+dd+'">'+dd+'</option>');
    }
      i = i+1;

  },
  displayDelete: function() {
    var deleteCnt = $('.delete').size();
    if (deleteCnt > 1) {
      $('.delete').show();
    } else {
      $('.delete').hide();
    }
  },
  displayTaxs: function() {
    var taxsCnt = $('#taxs tbody tr').size();
    if (taxsCnt > 0) {
      $('.tax-container').show();
    } else {
      $('.tax-container').hide();
    }
  }
};
// launc
Invoice.init();/**
 * Created by arjun on 4/14/2017.
 */
/**
 * Created by arjun on 4/18/2017.
 */
/**
 * Created by arjun on 4/19/2017.
 */
