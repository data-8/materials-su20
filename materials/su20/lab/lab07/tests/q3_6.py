test = {
  'name': 'q3_6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> rate_means.num_rows
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(rate_means.where("Death Penalty", False).column(1).item(0), 3)
          8.121
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(rate_means.where("Death Penalty", True).column(1).item(0), 3)
          7.514
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
