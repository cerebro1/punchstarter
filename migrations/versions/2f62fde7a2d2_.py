"""empty message

Revision ID: 2f62fde7a2d2
Revises: ef79c6c29854
Create Date: 2016-03-14 16:11:37.626481

"""

# revision identifiers, used by Alembic.
revision = '2f62fde7a2d2'
down_revision = 'ef79c6c29854'

from alembic import op  # NOQA
import sqlalchemy as sa  # NOQA


def upgrade():
    # commands auto generated by Alembic - please adjust!
    op.add_column('project', sa.Column('image_filename',
                                       sa.String(length=300), nullable=True))
    # end Alembic commands


def downgrade():
    # commands auto generated by Alembic - please adjust!
    op.drop_column('project', 'image_filename')
    # end Alembic commands
