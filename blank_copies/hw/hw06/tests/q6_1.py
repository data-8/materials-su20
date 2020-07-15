test = {
  'name': 'q6_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(bananas_given_apples, float)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> (bananas_given_apples >= 0) & (bananas_given_apples <= 1)
          True
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
