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
          >>> round(rate_means.where("Death Penalty", False).column(1).item(0), 4)
          8.1204
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(rate_means.where("Death Penalty", True).column(1).item(0), 4)
          7.5136
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
